# Dataset Name

Suggested citation: XXX.

## Data description

### Data documentation

The dataset is structured according to the ChildProject package standards detailed [here](https://childproject.readthedocs.io/en/latest/format.html).

### Participants & recordings

>Number of participants, general info on them.

>Number of recordings, specificities.

### Available annotations

>What sort of annotations are presents. 

**We strongly recommend the use of the `converted/` versions of the annotations, to avoid issues of time stamping and category assignment.**

#### Automated annotations
>keep relevant, add new ones if necessary

- alice: automated counts of phonemes, syllables, and words done by [ALICE](https://github.com/orasanen/ALICE); all recordings have been analyzed with this system
- its: automated analyses using the LENA software; only a small proportion of recordings (those gathered with a LENA device) have this annotation
- vcm: automated analyses aimed at categorization the key child's vocalizations into: canonical, non-canonical, crying, and other (which includes both "junk" = not the child at all; and laughing, which occurred infrequently), done using [VCM](https://github.com/srvk/DiViMe/blob/master/docs/source/tool_doc.md#vcm); all recordings have been analyzed with this system
- vtc: automated analyses that distinguish key child, other children, male adult, female adult, using [VTC](https://github.com/MarvinLvn/voice-type-classifier); all recordings have been analyzed with this system

#### Manual annotations
>explain what each set of manual annotation is and how it was produced
>Example from tsimane2017:
>- eaf_2021: A small number of recordings were selected for coding by two speech-and-language students unfamiliar with the language and the families recorded, who annotated randomly sampled 15-second sections, skipping any that failed to contain speech by male adults or other children, following [this coding manual](https://docs.google.com/document/d/19-EzpJNHT-pcagHm0-ZasAu2PzwT9j5lgz-SqC5zWTI/edit#heading=h.gt6kkkg2awdf), derived from the ACLEW Annotation Scheme, to do only segmentation.

## Getting access to the data

To gain access to the data, please email XXXX? or Homebank or ... ?


## Re-using the dataset

### Requirements

You will first need to install the ChildProject package as well as DataLad. Instructions to install these packages can be found [here](https://childproject.readthedocs.io/en/latest/install.html).

### Configuring your SSH key on GIN

This step should only be done once for all.

1. Copy your SSH public key to your clipboard (usually located in ~/.ssh/id_rsa.pub). If you don't have one, please create one following [these instructions](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
2. In your browser, go to [GIN > Your parameters > SSH keys](https://gin.g-node.org/user/settings/ssh).
3. Click on the blue "Add a key" button, then paste the content of your public key in the Content field, and submit.

Your key should now appear in your list of SSH keys - you can add as many as necessary.

### Installing the dataset

The next step is to clone the dataset :

```bash
datalad install git@gin.g-node.org:/LAAC-LSCP/XXX.git
cd XXX
```

### Getting data

You can get data from a dataset using the `datalad get` command, e.g.:

```bash
datalad get recordings/converted/ # download converted recordings
datalad get annotations/*/converted/ # get converted annotations
```

Or:

```bash
datalad get . # get everything
```

You can download many files in parallel using the -J or --jobs parameters:

```bash
datalad get . -J 4 # get everything, with 4 parallel transfers
```

For more help with using DataLad, please refer to our [cheatsheet](https://childproject.readthedocs.io/en/latest/cheatsheet.html) or DataLad's own [cheatsheet](http://handbook.datalad.org/en/latest/basics/101-136-cheatsheet.html). If this is not enough, check DataLad's [documentation](http://docs.datalad.org/en/stable/) and [Handbook](http://handbook.datalad.org/en/latest/).

### Fetching updates

If you are notified of changes to the data, please retrieve them by issuing the following commands:

```bash
datalad update --merge
datalad get .
```

### Removing the data

It is important that you delete the data once your project is complete.
This can be done with `datalad remove`:

```bash
datalad remove -r path/to/your/dataset
```


## Maintainers

Maintainers should install the dataset from LAAC-LSCP and run the setup procedure as follows:

```bash
datalad install git@gin.g-node.org:/LAAC-LSCP/tsimane2017.git
cd tsimane2017
datalad run-procedure setup --public --confidential
```

Changes should be pushed to origin, that will trigger a push to the others:

```bash
datalad push
```

## History

>History of the dataset, add an entry to explain what was done at this point in time, example (from tsimane2017):
- 2022-04 Alex Cristia processed files from Camila Scaff, resulting in data from XX children. These data came from copies of the back-up drives Lacie, hand-written notes, and re-listening to the audio files to determine date and child ID. Some of the processing was done by hand; other via a script called `gen-recordings.R`, which used to live in a dropbox folder shared between Alex and Camila.