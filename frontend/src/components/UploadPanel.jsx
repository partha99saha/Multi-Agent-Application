import { uploadFile } from "../services/api";

export default function UploadPanel() {

    const upload = async (e) => {

        const file = e.target.files[0];

        if (!file) return;

        await uploadFile(file);

        alert("Uploaded");

    };

    return (
        <div className="upload-panel">

            <input
                type="file"
                onChange={upload}
            />

        </div>
    );
}