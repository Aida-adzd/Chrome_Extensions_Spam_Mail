chrome.action.onClicked.addListener(function (tab) {
  chrome.tabs.create({ url: 'http://127.0.0.1:5000' });
});
