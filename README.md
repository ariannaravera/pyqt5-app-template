<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">VLabApplication</h3>

  <p align="center">
    Automating cellular image analysis
    <br />
    <a href="https://github.com/ariannaravera/pyqt_app_template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ariannaravera/pyqt_app_template">View Demo</a>
    ·
    <a href="https://github.com/ariannaravera/pyqt_app_template/issues">Report Bug</a>
    ·
    <a href="https://github.com/ariannaravera/pyqt_app_template/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center"><img src="support_files/Screenshot.png" alt="Logo" width="600"></div>

PyQt5 App template

<p align="right"><a href="#readme-top">back to top</a></p>


<!-- GETTING STARTED -->
## Getting Started

### Installation
The use of Anaconda is supposed.
 
1. Create a virtual environment for your code, in the terminal: 

  `conda create --name venv_VLabApp`
 
2. Once the venv is created, activate it: 
 
  `conda activate name_of_venv`

3. Clone this git repository. Open the terminal where you want to put the App code (eg. Desktop): 

  `git clone https://github.com/vjesticalab/VLabApp.git`
 
Now you have the VLabApp folder into the chosen directory (eg. Desktop/VLabApp)
 
4. Open the terminal within the VLabApp, activate your venv and install the libraries running:

  `conda install qt`
  `pip install -r requirements.txt`
 
  (If you have troubles with pyqt, try to install this and then the requirements.txt again:
  `pip install pyqt5 --config-settings --confirm-license= --verbose`)
 
Now you have everything you need to use the Application!

5. To open the application, run:
  
  `python3 master.py`


### Prerequisites

List of things you need to use the software and how to install them.
* PyQt5==5.15.9
* PyQt5_sip==12.12.1
* cellpose==2.2
* matplotlib==3.7.1
* napari==0.4.17
* nd2==0.5.3
* numpy==1.23.5
* opencv_python_headless==4.7.0.72
* pystackreg==0.2.7
* python_igraph==0.10.5
* QtPy==2.3.1
* roifile==2023.5.12
* scikit_image==0.19.3
* scipy==1.9.1
* tifffile==2023.4.12





<p align="right"><a href="#readme-top">back to top</a></p>


<!-- USAGE EXAMPLES -->
## Usage

<!-- 
Useful examples of how the application can be used. Additional screenshots, code examples and demos. Also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right"><a href="#readme-top">back to top</a></p>
-->


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="#readme-top">back to top</a></p>


<!-- LICENSE -->
## License

Distributed under the ... License. See `support_files/LICENSE.txt` for more information.

<p align="right"><a href="#readme-top">back to top</a></p>


<!-- CONTACT -->
## Contact

Arianna Ravera - ariannaravera22@gmail.com

Julien Dorier - 

Aleksandar Vjestica - 

Project Link: [VLabApp](https://github.com/vjesticalab/VLabApp)

<p align="right"><a href="#readme-top">back to top</a></p>


<!-- ACKNOWLEDGMENTS 
## Acknowledgments

Space to list helpful resources and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages eg.Cellpose](https://pages.github.com)

<p align="right"><a href="#readme-top">back to top</a></p>
-->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vjesticalab/Application.svg?style=for-the-badge
[contributors-url]: https://github.com/ariannaravera/pyqt_app_template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vjesticalab/Application.svg?style=for-the-badge
[forks-url]: https://github.com/ariannaravera/pyqt_app_template/network/members
[stars-shield]: https://img.shields.io/github/stars/vjesticalab/Application.svg?style=for-the-badge
[stars-url]: https://github.com/ariannaravera/pyqt_app_template/stargazers
[issues-shield]: https://img.shields.io/github/issues/vjesticalab/Application.svg?style=for-the-badge
[issues-url]: https://github.com/ariannaravera/pyqt_app_template/issues
[license-shield]: https://img.shields.io/github/license/vjesticalab/Application.svg?style=for-the-badge
[license-url]: https://github.com/ariannaravera/pyqt_app_template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/arianna-ravera-3a082917b
[product-screenshot]: support_files/Screenshot.png
[Python.com]: https://img.shields.io/badge/python-35495E?style=for-the-badge&logo=python&logoColor=green
[Python-url]: [https://pythonprogramminglanguage.com]
<!-- [JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com  -->
