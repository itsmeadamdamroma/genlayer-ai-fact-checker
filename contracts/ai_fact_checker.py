# { "Depends": "py-genlayer:test" }
import json
from genlayer import *


class AIFactChecker(gl.Contract):
    claims: TreeMap[str, str]
    reputation: TreeMap[Address, u256]

    def __init__(self):
        pass

    def _verify_claim(self, claim_text: str, source_url: str) -> dict:
        """AI-powered fact verification with Equivalence Principle"""
        def check_claim() -> str:
            web_data = gl.get_webpage(source_url, mode="text")
            task = f"""Analyze this claim against the provided web source.

CLAIM: {claim_text}

SOURCE CONTENT:
{web_data}

Respond ONLY in this exact JSON format, nothing else:
{{"verdict": "TRUE" or "FALSE" or "UNVERIFIABLE", "confidence": 85, "summary": "brief explanation max 100 words"}}
It is mandatory that you respond only using the JSON format above.
Your output must be only JSON without any formatting prefix or suffix.
This result should be perfectly parsable by a JSON parser without errors."""
            result = gl.exec_prompt(task)
            result = result.replace("```json", "").replace("```", "").strip()
            return json.dumps(json.loads(result), sort_keys=True)

        return json.loads(gl.eq_principle_strict_eq(check_claim))

    @gl.public.write
    def submit_claim(
        self, claim_id: str, claim_text: str, source_url: str
    ) -> None:
        """Submit a real-world claim for AI verification.

        The contract will:
        1. Fetch evidence from the source URL
        2. Use AI to analyze the claim against the evidence
        3. Reach consensus among validators using Equivalence Principle
        4. Store the verified result on-chain
        """
        if claim_id in self.claims:
            raise Exception("Claim ID already exists")

        result = self._verify_claim(claim_text, source_url)

        claim_data = json.dumps({
            "text": claim_text,
            "source": source_url,
            "verdict": result["verdict"],
            "confidence": result["confidence"],
            "summary": result["summary"],
            "submitter": gl.message.sender_address.as_hex
        }, sort_keys=True)

        self.claims[claim_id] = claim_data

        addr = gl.message.sender_address
        if addr not in self.reputation:
            self.reputation[addr] = u256(0)
        self.reputation[addr] += u256(1)

    @gl.public.view
    def get_claim(self, claim_id: str) -> str:
        """Retrieve a verified claim with its verdict and confidence score."""
        if claim_id not in self.claims:
            raise Exception("Claim not found")
        return self.claims[claim_id]

    @gl.public.view
    def get_all_claims(self) -> dict:
        """Get all verified claims stored on the contract."""
        return {k: v for k, v in self.claims.items()}

    @gl.public.view
    def get_reputation(self, address: str) -> int:
        """Check how many claims an address has submitted."""
        return int(self.reputation.get(Address(address), u256(0)))
