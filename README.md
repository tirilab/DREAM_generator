# DREAM Generator

## Environment Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd DREAM_generator
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ source venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

## OpenAI API Key

Please refer this [documentation](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key) to learn how to setup your OpenAI API Key.

After getting an API key use the command in the command line
```
export OPENAI_API_KEY='YOUR_API_KEY'
```
and change the `YOUR_API_KEY` with the actual API key.

## Run script

To generate message data, first replace the api_key in [script.py](https://github.com/tirilab/synthetic-patient-portal-message/blob/main/script.py). Then run the following comment under the project directory:

   ```bash
   $ python script.py -n [number of message data you want to generate] -f [file name of the synthetic messages] -tf [Taxonomy file name (in csv format)] -mf [Medicine list file name (in csv format)] -t [Taxonomy of the taxa3 as a string (optional: if you want to filter using taxa3 to generate messages of specific type)]
   ```

or use the command

   ```bash
   $ python script.py -h
   ```
for help on the flag usage.

## Data Samples
The taxonomy and medicine list files must be stored in assets folder.
A sample file for each is available in the assets folder.

## License and Citation

Data and script can be used as-is under the [MIT License](https://github.com/tirilab/DREAM_generator/blob/main/LICENSE) attached to the repository. Please cite this article if using this data or script:

Natalie Wang, Sukrit Treewaree, Ayah Zirikly, Yuzhi L. Lu, Michelle H. Nguyen, Bhavik Agarwal, Jash Shah, James Michael Stevenson, Casey Overby Taylor,
Taxonomy-based prompt engineering to generate synthetic drug-related patient portal messages,
Journal of Biomedical Informatics, Volume 160, 2024, 104752, ISSN 1532-0464, https://doi.org/10.1016/j.jbi.2024.104752.
