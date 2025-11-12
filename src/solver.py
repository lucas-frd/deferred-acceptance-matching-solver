class DeferredAcceptanceSolver:
    """Implements the Deferred Acceptance Algorithm for stable matching."""

    def __init__(
            self,
            proposal_preferences: list[list[int]],
            proposed_preferences: list[list[int]],
    ):
        self.proposal_preferences = proposal_preferences
        self.proposed_preferences = proposed_preferences
        self.matches = [-1] * len(proposal_preferences)
        
    def solve(self) -> list[int]:
        """Executes the Deferred Acceptance Algorithm and returns the matches."""
        unmatched_proposers = list(range(len(self.proposal_preferences)))
        while unmatched_proposers:
            proposer = unmatched_proposers.pop(0)
            top_choice = self.proposal_preferences[proposer][0]
            while not self._propose(proposer, top_choice):
                self.proposal_preferences[proposer].pop(0)
                top_choice = self.proposal_preferences[proposer][0]
            old_match = self.matches[top_choice]
            if old_match != -1:
                unmatched_proposers.append(old_match)
            self.matches[top_choice] = proposer
        return self.matches
    
    def _propose(self, proposer: int, proposed: int) -> bool:
        """Handles a proposal from a proposer to a proposed."""
        current_match = self.matches[proposed]
        if current_match == -1:
            return True
        proposed_pref = self.proposed_preferences[proposed]
        if proposed_pref.index(proposer) < proposed_pref.index(current_match):
            return True
        return False
    

