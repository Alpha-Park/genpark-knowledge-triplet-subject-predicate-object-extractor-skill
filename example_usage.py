import json
from client import KnowledgeTripletSPOExtractor

def main():
    extractor = KnowledgeTripletSPOExtractor()
    text = "Satya joined Microsoft in 1992 and relocated to Seattle."
    result = extractor.extract_triplets(text)
    print("Extracted SPO Triplets:")
    print(json.dumps(result, indent=2))
    assert result["triplets_extracted_count"] == 2
    assert result["triplets"][0]["predicate"] == "works_at"
    assert result["triplets"][1]["predicate"] == "lives_in"
    print("Knowledge triplet extractor verification: PASS")

if __name__ == "__main__":
    main()
