// main.js
const { app, BrowserWindow, screen } = require('electron');
const express = require('express');
const server = express();
const PORT = 8000;



// サーバーのセットアップ
server.get('/', (req, res) => {
    res.send('Hello from the server!');
});

// Electronのウィンドウを作成

function createWindow() {
    // プライマリディスプレイの解像度を取得
    const primaryDisplay = screen.getPrimaryDisplay();
    const { width, height } = primaryDisplay.workAreaSize;

    const win = new BrowserWindow({
        width: width,
        height: height,
        minWidth: 800, // 最小幅を800に設定
        minHeight: 600, // 最小高さを600に設定
        frame: true, // ウィンドウのフレームを非表示にする
        webPreferences: {
            nodeIntegration: true
        }
    });

    // ローカルサーバーにアクセス
    win.loadURL(`http://127.0.0.1:${PORT}`);
}

// Electronの初期化とローカルサーバーの起動
app.whenReady().then(() => {
    server.listen(PORT, () => {
        console.log(`Server running on http://127.0.0.1:${PORT}`);
        createWindow();
    });

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
