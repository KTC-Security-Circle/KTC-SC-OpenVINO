document.addEventListener('DOMContentLoaded', function () {
    var fileInput = document.querySelector('input[type="file"]');
    var video = document.getElementById('selected-video');

    fileInput.addEventListener('change', function(e) {
        var file = e.target.files[0];

        if (file && file.type.startsWith('video/')) {
            var url = URL.createObjectURL(file);
            video.src = url;
            video.style.display = 'block';
            video.load();
        } else {
            video.style.display = 'none';
        }
    });
});
document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();

    var formData = new FormData(this);

    // オーバーレイ表示
    document.getElementById('overlay').style.display = 'block';

    fetch(this.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // 応答をJSONとして解析
    .then(data => {
        window.location.href = data.redirectUrl; // リダイレクト先のURLを設定
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('overlay').style.display = 'none';
    });
});
