from paralex import paralex_factory

freq_antiquitas = {"name": "frequency_Antiquitas",
                   "title": "Frequency in the Antiquitas",
                   "description": "The frequency of this item in the Antiquitas epoch "
                                  "in Tombeur's Thesaurus (from the origins to the end of the 2nd century A.D.)",
                   "type": "number"
                   }
freq_aetaspatrum = {"name": "frequency_AetasPatrum",
                    "title": "Frequency in the Aetas Patrum",
                    "description": "The frequency of this item in the Aetas Patrum epoch "
                                   "in Tombeur's Thesaurus (2nd century-735 A.D.)",
                    "type": "number"
                    }
freq_mediumAeuum = {"name": "frequency_MediumAeuum",
                    "title": "Frequency in the Medium Aeuum",
                    "description": "The frequency of this item in the Medium Aeuum epoch "
                                   "in Tombeur's Thesaurus (736-1499)",
                    "type": "number"
                    }
freq_recentior = {"name": "frequency_RecentiorLatinitas",
                  "title": "Frequency in the Recentior Latinitas",
                  "description": "The frequency of this item in the Recention Latinitas epoch "
                                 "in Tombeur's Thesaurus (1500-1965)",
                  "type": "number"
                  }

freq_cols = [freq_antiquitas, freq_aetaspatrum, freq_mediumAeuum, freq_recentior]

package = paralex_factory("LatInfLexi",
                          {
                              "forms": {"path": "LatInfLexi-forms.csv",
                                        "schema": {"fields": freq_cols}
                                        },
                              "cells": {"path": "LatInfLexi-cells.csv",
                                        "schema": {
                                            "fields": [{"name": "cell_romance_aligned",
                                                        "title": "cell code in OODRVM",
                                                        "description": "The code used for this cell in the Oxford Online Database of Romance Verb Morphology",
                                                        "type": "string"
                                                        },
                                                       {"name": "cell_LatInfLexi_v1",
                                                        "title": "cell code in LatInfLexi v1.1",
                                                        "description": "The code used for this cell in the previous release of LatInfLexi (v1.1)",
                                                        "type": "string"
                                                        }
                                                       ] + freq_cols
                                        }
                                        },
                              "features-values": {"path": "LatInfLexi-features-values.csv"},
                              "sounds": {"path": "LatInfLexi-sounds.csv"},
                              "graphemes": {"path": "LatInfLexi-graphemes.csv"},
                              "lexemes": {"path": "LatInfLexi-lexemes.csv",
                                          "schema": {"fields": freq_cols}
                                          }
                          },
                          citation="Pellegrini, M. & Passarotti, M. & Beniamine, S. (2023). LatInfLexi 2.0. Online.",
                          version="2.0",
                          keywords=["Latin", "verbs", "nouns", "paradigms", "cells"],
                          id="?",
                          contributors=[{'title': 'Matteo Pellegrini', 'role': 'author'},
                                        {'title': 'Marco Passarotti', 'role': 'contributor'},
                                        {'title': 'Sacha Beniamine', 'role': 'contributor'}],
                          licenses=[{'name': 'CC BY-SA 4.0 DEED',
                                     'title': 'Creative Commons Attribution-ShareAlike 4.0 International',
                                     'path': 'https://creativecommons.org/licenses/by-sa/4.0/'}]
                          )
package.to_json("LatInfLexi_package.json")
