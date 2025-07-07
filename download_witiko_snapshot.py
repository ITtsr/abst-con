from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="witiko/mathberta",
    local_dir="models/mathberta",
    repo_type="model"
)