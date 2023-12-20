Data set name: LatInfLexi 2.0

Citation: Pellegrini, M. & Passarotti, M. & Beniamine, S. (2023). LatInfLexi 2.0. Online.

Data set developers: Matteo Pellegrini, Marco Passarotti, Sacha Beniamine

Data sheet author: Matteo Pellegrini

# Motivation

**For what purpose was the dataset created?** 

This dataset was originally created to allow for a quantitative analysis of predictability in implicative relations between paradigm cells of Latin verbs and nouns. 

**Who created the dataset (for example, which team, research group) and on behalf of which entity (for example, company, institution, organization)?**

This dataset was created by Matteo Pellegrini as part of his PhD, supervised by Pierluigi Cuzzolin at the University of Bergamo.

# Composition

Paralex datasets document paradigms of inflected forms.

**Are forms given as orthographic, phonetic, and or phonemic sequences ?**

Forms are given both in orthographic and phonetich transcription.

**How many instances are there in total?**

- Number of inflected forms: 816,985 (including defective cells)
- Number of lexemes: 4,387
- Maximal paradigm size in cells: 254 (for verbs), 12 (for nouns) 

**Language varieties** 

-   BCP-47 language tag: lat
-   Language variety description: Latin, mostly as spoken in the Classical, Pre-Classical and Post-Classical times

**Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** 

The dataset consists of the inflected forms of a sample of the lexemes included in the database of Lemlat 3.0. The sampling is based:
- on diachrony, i.e., only items included in the "base" section of the database -- roughly corresponding to Classical, Pre-Classical and Post-Classical times -- are included, excluding items pertaining to Medieval Latin;
- on frequency, i.e., only the 3,348 verbs attested in Delatte et al.'s (1981) *Dictionnaire fréquentiel et Index inverse de la langue latine*, and the 1,038 most frequent nouns in the same resource are included.

**Is any information missing from individual instances?** 

Verbs that are explicitly marked as impersonals in our data source are coded as defective of non-3rd person singular finite forms.
Verbs that are explicitly marked as deponents in our data source are coded as defective of morphologically active forms.
Verbs that are explicitly marked as "perfectum tantum" in our data source are coded as defective of imperfective forms.
Nouns that are explicitly marked as "pluralia tantum" in our data source are coded as defective of singular forms.
Missing forms that are not marked as defective should be interpreted as missing data that cannot be generated on the basis of the information provided by our data source.

**Are there any errors, sources of noise, or redundancies in the dataset?** If so, please provide a description.

There is no systematic source of errors, noise or redundancy in the dataset (although of course there probably are occasional mistakes).
No explicit indication of (un)certainty is expressed, as the same procedure is applied to obtain all forms in the dataset.

**Is the dataset self-contained, or does it link to or otherwise rely on external resources (for example, websites, tweets, other datasets)?**

The dataset is self-contained.

# Collection process.

**What is provenance for each table (lexemes, cells, forms, frequencies, sounds, features), as well as for segmentation marks if any ? Are any information derived from other datasets ?**

The forms have been generated exploiting the information provided in the database of a morphological analyzer of Latin, Lemlat 3.0 (https://github.com/CIRCSE/LEMLAT3).
The frequencies have been obtained from Tombeur's (1998) *Thesaurus Formarum Totius Latinitatis*.
The feature-value specifications for sounds are based on Cser (2020) *The Phonology of Classical Latin*, with some adaptations, mostly to account for the sounds that are present in this database but not in Cser's account -- e.g., aspirated consonants.
The feature-value specifications for cells are based on the categories used in most traditional descriptions of Latin.

**How were paradigms separated between lexemes (eg. in the case of homonyms or variants) ? What theoretical or practical choices were made ?**

The assignment of forms to lexemes reflects the information that can be inferred from our data source.

**How was the paradigm structure (set and labels of paradigm cells) decided ? What theoretical or practical choices were made ?**

The dataset includes all the cells that are filled by a synthetic form: cells that are always filled by a periphrase (e.g., all perfective forms of Latin verbs) are excluded.
For nouns, the locative is excluded because of its marginality.

**What is the expertise of the contributors with the documented language ?**

Matteo Pellegrini and Marco Passarotti are experts of the Latin language.

**Who was involved in the data collection process (for example, students, crowdworkers, contractors) and how were they compensated (for example, how much were crowdworkers paid)?**

Matteo Pellegrini and Marco Passarotti were involved in the data generation process.
Sacha Beniamine was involved in the addition of stress to phonetic transcriptions and in various aspects related to the conversion into Paralex format.

**Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (for example, recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.

The work for the creation of this resource has been carried out during Matteo Pellegrini's PhD (2016-2020).
The data of this resource have been obtained from the database of Lemlat 3.0, as documented in Passarotti, M & Budassi, M & Litta, E. & Ruffolo, P. 2017. *The Lemlat 3.0 Package for Morphological Analysis of Latin*. Proceedings of the NoDaLiDa 2017 Workshop on Processing Historical Language.

**Were any ethical review processes conducted (for example, by an institutional review board)?** If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.

No ethical review process was needed.

# Preprocessing/cleaning/labeling.

**How were frequencies measured ?** 

The frequencies have been obtained from Tombeur's (1998) *Thesaurus Formarum Totius Latinitatis*.

**How were the inflected forms obtained ?** 

The forms have been generated exploiting the information provided in the database of a morphological analyzer of Latin, Lemlat 3.0 (https://github.com/CIRCSE/LEMLAT3).

**How were the phonological or phonemic transcriptions obtained ?**

The phonetic transcriptions have been obtained semi-automatically on the basis of orthographic transcriptions.

# Uses

**Has the dataset been used for any published work already?** 

The dataset (in its previous version) has been used for several publications on paradigm structure in Latin by Matteo Pellegrini and collaborators. The most up-to-date and complete analysis can be found in Pellegrini. 2023. *Paradigm Structure and Predictability in Latin Inflection. An Entropy-based Approach*.
It has also been used to supply information on Latin for the Oxford Online Database of Romance Verb Morphology (Beniamine, Maiden & Round. 2020. Opening the Romance Verbal Inflection Dataset 2.0: a CLDF Lexicon. https://aclanthology.org/2020.lrec-1.370.pdf)

# Distribution.

**How will the dataset be distributed (for example, tarball on website, API, GitHub)?** Does the dataset have a digital object identifier (DOI)?

The dataset is released in this Zenodo repository as a set of .csv files following the Paralex standard format for paradigmatic lexicons.

**When will the dataset be distributed?**

The dataset is already available.

**Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** 

The dataset is distributed under a Creative Commons-Attribution-ShareAlike 4.0 International license (https://creativecommons.org/licenses/by-sa/4.0/).

# Maintenance

**Who will be supporting/hosting/maintaining the dataset?**

The dataset is maintained by Matteo Pellegrini.

**How can the owner/curator/manager of the dataset be contacted (for example, email address)?**

The curator of the dataset can be contacted by email at matteo.pellegrini@unicatt.it.

**Will the dataset be updated (for example, to correct labeling errors, add new instances, delete instances)?** If so, please describe how often, by whom, and how updates will be communicated to dataset consumers (for example, mailing list, GitHub)?

The dataset will be updated whenever significant changes will be done. This will be communicated to dataset consumers in the GitHub repository.
