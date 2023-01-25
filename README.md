# raag.ai
Raag Kirtan (classical Sikh music tradition) classification project using a Convulutional Neural Network (CNN)


## What Is Raag Kirtan?

Raag Kirtan is a form of devotional music in the Sikh Tradition. It involves chanting of scripture from Sri Guru Granth Sahib in specific “Raags” to invoke a spiritual state in the listener/singer. A Raag is set of musical modes in Indian classical music and cover a variety of different sub-genres representing different moods, times of day, weather and even seasons. he word “Raag” itself refers to the ‘rhythm’ and ‘melody’ or ‘colour’. Each Raag has its own distinct character, with set of rules and regulations governing its form.

The Sri Guru Granth Sahib (primary scripture of the Sikhs) is itself divided in sections attributed to the different Raags. There are a total of 60 Raags present in it and Shabads (hymns) from each section are sung in the appropriate Raag. 

## What is Raag.ai?

This project aims to provide a classification tool that can be given a sample of a Raag Kirtan track and make a prediction as to what Raag it is. The motivation behind this is that over the last few centuries Sikh Raag Kirtan traditions have been in decline and instead Shabads are sung through more simpler and bollywood-esque styles. This is unfortunate since the writers of those Shabads had specifically designed them in a way to be sung in the accompanying Raag specified. However, by ignoring that crucial aspect, much of the original feelings and moods it was meant to portray gets lost. Therefore, this project aims to help reinvigorate interest for this important area of Sikh tradition and support those on the forefront of revitalising this diminishing art. 

In time I hope this project could evolve in providing further use cases incorporating Raag and AI. Some examples of this could include:

- Ability to sort playlist that organises tracks based on similar Raags,
- Live audio input feature where someone could sing and the program could guess what Raag it is.
    - This could potentially help people learning Raag Kirtan to practice or score themselves.

## Challenges

- Collecting good data and enough tracks to represent each Raag.
- Identifying which parts of a track reveals what Raag it is in.
- Learning which model is most effective and how best to tune hyperparameters to improve accuracy.
- Improving the model to encompass a real-time data input (via microphone).
- Establish a GUI / Front-end application so that this is accessible and interactive.

## How it Works

1. dir_maker.py
    
    First I created a directory called “Data”, within that I included 3 folders: “instrument_only”, “vocals only” and “kirtan” (vocals and instruments). The primary folder I used to train the model so far has been “kirtan”. This is because these are the most common for Sikh Raag Kirtan, however since the underlying Raag tradition is also shared by the wider Indian community, I may also incorporate tracks from outside just Sikh kirtan to help train the model on more examples of Raags in future.
    
    The dir_maker.py script creates further directories for each one of the 60 Raags.
    
2. yt_mp3.py  
    
    Then I used the pytube package to help quickly download and convert YouTube videos of Raag Kirtan into mp3 tracks. This script is run and saved directly into the corresponding Raag folder
    
    The directory structures is as follows:
    
    ```
    
    Data > instrument_only 
         > vocals_only
         > kirtan > Asa 
                   > Asa Asavari
                   > Asa Kafi
                   > (…) (Raag Names)
                   > Vadhans Dakhani > Example_Raag_Vadhans_Dakhani_Track_1.mp3
                                     > Example_Raag_Vadhans_Dakhani_Track_2.mp3
                                     > (…)
                         
    ```
    
    As of 25/01/23, only the following Raags have samples saved:
    
    ['Asa', 'Asa Kafi', 'Asavari', 'Bairarri', 'Basant', 'Dhanasri']
    
    The full folder directory containing the data could not be uploaded to Github due to size constraints. 
    
    **TO DO:** Upload to Google Drive / cloud storage
   
    
3. data_prep.ipynb
    
    Here I prepare the data using the librosa package by cutting the tracks into a number of equal sized pieces. I then create a series of matrices from them using melspectrogram fucntion in the librosa package. I collect these and assign the appropriate Raag label based on what folder the original pre-cut track was in. This then gives me a number of samples with corresponding labels ready for machine learning.
    
4. model_training.ipynb
    
    Here I import the prepared data (saved previously as .pkl files) and label encode the Raag classes. After that, I split the data in train, test and validation sets before building a neural network to train a model to recognise the difference between each raag track.
    
    **Results:**
    
    The final epoch (30/30) had an accuracy of 97.9% on the training set and 88.5% on the validation set. 
    
    On the test set, the accuracy was 88.7%.
    
    This is quite good considering the tracks were not pre-processed to cut out introductions, midway speeches or YouTube       channel intro music yet. Additionally there are only a handful of tracks in each of the Raag categories so far.
    

## Next Steps

- Add more Kirtan tracks
- Experiment and tune parameters
- Establish a user interface to upload new tracks to predict
