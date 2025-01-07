document.getElementById("upload-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append("job_id", document.getElementById("job-id").value);
    formData.append("resume", document.getElementById("resume").files[0]);

    const response = await fetch("http://127.0.0.1:5000/upload_resume", {
        method: "POST",
        body: formData
    });

    const results = await response.json();
    document.getElementById("results").innerText = JSON.stringify(results, null, 2);
});
