## *CAN**DATA**PLOTTER*

Graphical user interface for the Can Data gathered through python. This application allows to view data gathered through a can device in plot and list form.

#### The main features are:

- Real-time plotting and monitoring of can data 
- Built on PyQt5

### Installation

1. Install Python if you don't have it installed yet
    - We suggest to use Anaconda. [Here is how to install it.](https://docs.anaconda.com/anaconda/install/)
    - Once you have your Anaconda running open your terminal (on windows anaconda prompt) and run:
    ```sh
    conda create -n can-bus python=3.6
    ```
    - Once this is done you will never have to run that command again, from now on you will just need:
    ```sh
    conda activate can-bus
    ```
2. Clone this repository or download the zip file

3. Enter the folder containing the repository using the terminal
    -  the command will be something like this:
    ```sh
    cd  some_path_on_disk/jbmcangui
    ```
4. Final step of the installation is installing all the necessary libraries for the *CAN**DATA**PLOTTER* :
    ```sh
    pip install -r "requirements.txt"
    ```

Once you have done all the steps above you do not need to repeat them any more. All you need to do the next time is open your terminal in the *CAN**DATA**PLOTTER* directory and run the command:
```sh
python main.py
```
Or if using Anaconda:
```sh   
conda activate can-bus
python main.py
```


### Usage

*CAN**DATA**PLOTTER* has several useful features:

- A simple approach to plotting or view your data
  - Select the Plot/ List view from the top left corner
  - Select the DBC file with which you want the data to be decoded
  - As long as you're getting data through the can the plotting should start




