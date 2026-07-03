# 💾 Volumes Example

This showcase feature demonstrates persistent storage on Infra-Heroes via a `[[volumes]]` mount in `hero.toml`.

## 🛠️ Project Structure

- `main.py`: A Flask app with a form that writes a message to `/app/data/test.txt` and displays the file's current contents.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with a `data-vol` volume mounted at `/app/data`.

## 🚀 Deployment & Usage

1. Deploy the app:
   ```bash
   cd features/volumes
   heroctl deploy --project default
   ```
2. Open the deployed URL, type a message into the form, and submit it.
3. Redeploy or restart the service (`heroctl restart`) and reload the page — the message you saved should still be there, confirming `/app/data` is backed by a persistent volume rather than the container's ephemeral filesystem.
