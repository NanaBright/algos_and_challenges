using System;
using System.Collections.Generic;

class Document {
    public int Id { get; set; }
    public string Text { get; set; }
}

class BooleanSearch {
    static void Main(string[] args) {
        // Define some sample documents
        List<Document> documents = new List<Document> {
            new Document { Id = 1, Text = "The quick brown fox jumps over the lazy dog" },
            new Document { Id = 2, Text = "A bird in the hand is worth two in the bush" },
            new Document { Id = 3, Text = "An apple a day keeps the doctor away" },
            new Document { Id = 4, Text = "The early bird catches the worm" }
        };

        // Perform a Boolean search for documents containing the keywords "bird" AND "apple"
        List<Document> results = BooleanSearchQuery(documents, "bird", "apple");

        // Display the results
        Console.WriteLine("Results:");
        foreach (var doc in results) {
            Console.WriteLine(doc.Text);
        }
    }

    static List<Document> BooleanSearchQuery(List<Document> documents, params string[] keywords) {
        List<Document> results = new List<Document>();
        foreach (var doc in documents) {
            bool matches = true;
            foreach (var keyword in keywords) {
                if (!doc.Text.Contains(keyword)) {
                    matches = false;
                    break;
                }
            }
            if (matches) {
                results.Add(doc);
            }
        }
        return results;
    }
}
