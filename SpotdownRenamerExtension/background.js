
chrome.downloads.onDeterminingFilename.addListener(
  (download, suggest) => {
    const nombre = download.filename.split(/[\\/]/).pop();

    if (!nombre.includes("_spotdown.org")) {
      suggest();
      return;
    }

    suggest({
      filename: nombre.replace(/_spotdown\.org/g, ""),
      conflictAction: "uniquify"
    });
  }
);
