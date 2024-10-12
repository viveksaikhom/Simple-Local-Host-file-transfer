# Flask File Upload and Download Application

This is a simple Flask application that allows users to upload and download files within the same network. The application supports multiple file uploads and provides a list of uploaded files for download. It is also mobile-friendly, working seamlessly across different devices.

## Features

- Upload multiple files at once via drag-and-drop or file selection.
- View a list of uploaded files for download.
- Displays upload progress and speed.
- Mobile-friendly interface for use on various devices.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.

   ```bash
   cd your-project-directory
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:

   ```bash
   pip install Flask
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000` or `http://<your-ip-address>:5000` if accessing from another device on the same network.

3. Use the upload form to select and upload files by dragging them into the designated area or clicking the "Choose Files" button.

4. View the list of uploaded files and click on any file to download it.

## Directory Structure

```
your-project-directory/
│
├── app.py              # The main Flask application file
├── Recent Files        # Directory for uploaded files (If not it will create automatically)
└── templates/
    └── index.html      # HTML template for the main page
```

### `index.html`

The `index.html` file provides a user-friendly interface for uploading and downloading files. It includes:

- A drag-and-drop area for file uploads.
- A button to select files from the system.
- A progress bar to display the upload status and speed.
- A list of available files for download.
- Responsive design for mobile-friendly access.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
```

Feel free to let me know if you need any more changes or additions!
