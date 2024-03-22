document.addEventListener("DOMContentLoaded", function () {
  const addBookmarkButton = document.getElementById("addBookmark");
  const bookmarkList = document.getElementById("bookmarkList");
  let counter = 1;

  addBookmarkButton.addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      const { title, url } = tabs[0];
      chrome.storage.sync.get("bookmarks", function (data) {
        const bookmarks = data.bookmarks || [];
        bookmarks.push({ id: counter++, title, url }); // Assigning unique id to each bookmark
        chrome.storage.sync.set({ bookmarks }, function () {
          displayBookmarks(bookmarks);
        });
      });
    });
  });

  function displayBookmarks(bookmarks) {
    bookmarkList.innerHTML = "";
    bookmarks.forEach(function (bookmark, index) {
      const item = document.createElement("li");
      item.classList.add("bookmark-item");
      item.innerHTML = `
        <div class="bookmark-content">
          <span class="bookmark-number">${bookmark.id}</span>
          <a href="${bookmark.url}" target="_blank" class="bookmark-link">${bookmark.title}</a>
          <button class="deleteBookmark btn-warning" data-index="${index}">Delete</button>
        </div>`;
      bookmarkList.appendChild(item);
    });

    const deleteButtons = document.getElementsByClassName("deleteBookmark");
    Array.from(deleteButtons).forEach(function (button) {
      button.addEventListener("click", function () {
        const index = parseInt(button.getAttribute("data-index"));
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
