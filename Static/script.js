const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const btn = document.getElementById("btn");
const out = document.getElementById("out");

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream);

btn.onclick = async () => {
    const ctx = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);

    const blob = await new Promise(r => canvas.toBlob(r, "image/jpeg"));

    const form = new FormData();
    form.append("file", blob);

    const res = await fetch("/analyze", {
        method: "POST",
        body: form
    });

    out.textContent = JSON.stringify(await res.json(), null, 2);
};
