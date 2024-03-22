document.addEventListener("DOMContentLoaded", function () {
  const addBookmarkButton = document.getElementById("addBookmark");
  const bookmarkList = document.getElementById("bookmarkList");

  addBookmarkButton.addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      const { title, url } = tabs[0];
      chrome.storage.sync.get("bookmarks", function (data) {
        const bookmarks = data.bookmarks || [];
        bookmarks.push({ title, url });
        chrome.storage.sync.set({ bookmarks }, function () {
          displayBookmarks(bookmarks);
        });
      });
    });
  });

  function displayBookmarks(bookmarks) {
    bookmarkList.innerHTML = "";
    bookmarks.forEach(function (bookmark) {
      const item = document.createElement("li");
      item.innerHTML = `<a href="${bookmark.url}" target="_blank">${bookmark.title}</a> <button class="deleteBookmark">Delete</button>`;
      bookmarkList.appendChild(item);
    });

    const deleteButtons = document.getElementsByClassName("deleteBookmark");
    Array.from(deleteButtons).forEach(function (button, index) {
      button.addEventListener("click", function () {
        chrome.storage.sync.get("bookmarks", function (data) {
          const updatedBookmarks = data.bookmarks.filter((_, i) => i !== index);
          chrome.storage.sync.set({ bookmarks: updatedBookmarks }, function () {
            displayBookmarks(updatedBookmarks);
          });
        });
      });
    });
  }

  chrome.storage.sync.get("bookmarks", function (data) {
    displayBookmarks(data.bookmarks || []);
  });
});
