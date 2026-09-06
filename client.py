import re
from typing import Dict, Any, List, Optional

class KnowledgeTripletSPOExtractor:
    """
    Parses conversational text and extracts canonical (Subject, Predicate, Object)
    knowledge graph assertion triplets using regex structural heuristics.
    """
    RELATION_PATTERNS = [
        (r"\b([A-Z][a-zA-Z]+)\s+(works at|is employed by|joined)\s+([A-Z][a-zA-Z0-9]+)\b", "works_at"),
        (r"\b([A-Z][a-zA-Z]+)\s+(founded|created|built)\s+([A-Z][a-zA-Z0-9]+)\b", "founded"),
        (r"\b([A-Z][a-zA-Z]+)\s+(prefers|likes|uses)\s+([A-Z][a-zA-Z0-9]+|[a-z]+)\b", "prefers"),
        (r"\b([A-Z][a-zA-Z]+)\s+(lives in|relocated to|moved to)\s+([A-Z][a-zA-Z]+)\b", "lives_in")
    ]

    def extract_triplets(self, text: str) -> Dict[str, Any]:
        triplets = []

        for pattern, predicate_name in self.RELATION_PATTERNS:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                subj = match.group(1).capitalize()
                obj = match.group(3).capitalize()
                triplets.append({
                    "subject": subj,
                    "predicate": predicate_name,
                    "object": obj,
                    "raw_match": match.group(0)
                })

        return {
            "input_text": text,
            "triplets_extracted_count": len(triplets),
            "triplets": triplets
        }
