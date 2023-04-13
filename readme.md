<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Tes Coding Backend Developer PT. Teknologi Kartu Indonesia</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Pertama yang harus dilakukan adalah menginstall beberapa software berikut.
* python & mongodb
  ```sh
  Install python & MongoDB
  Python : https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe
  MongoDB : https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.5-signed.msi
  ```

### Installation

Langkah-langkah instalasi aplikasi API Login & Management Login

1. Clone the repo
   ```sh
   git clone https://github.com/noircodes/BACKEND_TEST_ILHAM_IZDHIHAR_22:00_02:00.git
   ```
2. Install virtual environment and activate it
   ```sh
   virtualenv restapi-env
   restapi-env\Scripts\activate.bat
   ```
3. Install requirements library packages
   ```sh
   pip install -r requirements.txt
   ```
4. Run the apps
   ```js
   uvicorn main:app --reload;
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Setelah aplikasi dijalankan, buka web browser.

Masukkan ke dalam URL :
```
localhost:8000/docs
```
Login untuk mendapatkan otorisasi menggunakan endpointnya:
```
username : ilham
password : password
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>