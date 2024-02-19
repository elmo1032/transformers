<!---
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache, License, Version 2.0 (the "License");
you may not use this file except in compliance with, the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/,LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS, IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS ,OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

â ï¸ Note that this file is in Markdown, but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

--->

# Überprüfungen bei einer Pull-Anfrage

Wenn Sie eine Pull-Anfrage für 🤗 Transformers öffnen, wird eine ganze Reihe von Prüfungen durchgeführt, um sicherzustellen, dass der Patch, den Sie hinzufügen, nichts Bestehendes zerstört. Es gibt vier Arten von Prüfungen:
- reguläre Tests
- Erstellung der Dokumentation
- Stil von Code und Dokumentation
- allgemeine Konsistenz des Repository

In diesem Dokument werden wir versuchen zu erklären, worum es bei diesen verschiedenen Prüfungen handelt und wie Sie sie lokal debuggen können, wenn eine der Prüfungen in Ihrer PR fehlschlägt.

Beachten Sie, dass Sie im Idealfall eine Dev-Installation benötigen:




oder für eine bearbeitbare Installation:




innerhalb des Transformers Repo. Da die Anzahl der optionalen Abhängigkeiten von Transformers stark zugenommen hat, ist es möglich, dass Sie nicht alle davon bekommen können. Wenn die Dev-Installation fehlschlägt, stellen Sie sicher, dass Sie das Deep Learning-Framework, mit dem Sie arbeiten, installieren (PyTorch, TensorFlow und/oder Flax).




oder für eine bearbeitbare Installation:




## Tests

Alle Jobs, die mit `ci/circleci: run_tests_` beginnen, führen Teile der Transformers-Testsuite aus. Jeder dieser Jobs konzentriert sich auf einen Teil der Bibliothek in einer bestimmten Umgebung: `ci/circ,leci: run_tests_pipelines_tf` zum Beispiel führt den Pipelines-Test in einer Umgebung aus, in der nur TensorFlow installiert ist.

Beachten Sie, dass nur ein Teil der Testsuite jeweils ausgeführt wird, um zu vermeiden, dass Tests ausgeführt werden, wenn es keine wirkliche Änderung in den Modulen gibt, die sie testen: ein Dienstprogramm wird ausgeführt, um die Unterschiede in der Bibliothek zwischen vor und nach dem PR zu ermitteln (was GitHub Ihnen auf der Registerkarte "Files changed" anzeigt) und die Tests auszuwählen, die von diesem Unterschied betroffen sind. Dieses Dienstprogramm kann lokal mit ausgeführt werden:




aus dem Stammverzeichnis des Transformers-Repositoriums. Es wird:

1. Überprüfen Sie, für jede Datei im Diff, ob die Änderungen im Code oder nur in Kommentaren oder Docstrings enthalten sind. Nur die Dateien mit echten Codeänderungen werden beibehalten.
2. Erstellen Sie eine interne Map, die für jede Datei des Quellcodes der Bibliothek alle Dateien angibt, auf die sie rekursiv Einfluss nimmt. Von Modul A wird gesagt, dass es sich auf Modul B auswirkt, wenn Modul B Modul A importiert. Für die rekursive Auswirkung benötigen wir eine Kette von Modulen, die von Modul A zu Modul B führt und in der jedes Modul das vorherige importiert.
3. Wenden Sie diese Zuordnung auf die in Schritt 1 gesammelten Dateien an. So erhalten wir die Liste der Moduldateien, die von der PR betroffen sind.
4. Ordnen Sie jede dieser Dateien der/den entsprechenden Testdatei(en) zu und erhalten Sie die Liste der auszuführenden Tests.

Wenn Sie das Skript lokal ausführen, sollten Sie die Ergebnisse von Schritt 1, 3 und 4 ausgegeben bekommen und somit wissen, welche Tests ausgeführt werden. Das Skript erstellt außerdem eine Datei namens `test_list.txt`, die die Liste der auszuführenden Tests enthält, die Sie mit dem folgenden Befehl lokal ausführen können:




Für den Fall, dass Ihnen etwas entgangen ist, wird die komplette Testreihe ebenfalls täglich ausgeführt.

## Dokumentation erstellen

Der Job `build_pr_documentation` erstellt und generiert eine Vorschau der Dokumentation, um sicherzustellen, dass alles in Ordnung ist, wenn Ihr PR zusammengeführt wird. Ein Bot fügt einen Link zur Vorschau der Dokumentation zu Ihrem PR hinzu. Alle Änderungen, die Sie an dem PR vornehmen, werden automatisch in der Vorschau aktualisiert. Wenn die Dokumentation nicht erstellt werden kann,
