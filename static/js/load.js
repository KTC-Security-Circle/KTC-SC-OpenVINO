document.addEventListener('DOMContentLoaded', function() {
    const overlayButton = document.getElementById('overlayButton');
    const fileInput = document.getElementById('file-input');
    var overlay = document.getElementById("overlay");
    var closeOverlayButton = document.getElementById("closeOverlayButton");

    if (overlayButton) {
        overlayButton.addEventListener('click', function() {
            if (fileInput.files.length === 0) {
                alert('動画ファイルを選択してください。');
                return false;
            }
            overlay.style.display = "flex";
            setTimeout(function () {
                var result = confirm(
                    "推論が完了しました。結果ページに移動します。キャンセルすると、推論結果は破棄され最初から開始されます。"
                );
                if (result) {
                    window.location.href = "obj_result";
                    overlay.style.display = "none";
                }
            }, 5000);
        });
    }

    if (closeOverlayButton) {
        closeOverlayButton.addEventListener("click", function () {
            overlay.style.display = "none";
        });
    }
});
document.querySelector('#upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var formData = new FormData(e.target);
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
  });