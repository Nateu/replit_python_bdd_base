from mamba import description, context, it, before
from expects import expect, equal
from package import NewClass

with description("Given a NewClass") as self:
    with before.each:
        self.myClass = NewClass()

    with context("When nothing else happens"):
        with it("Should be an instance of NewClass"):
            expect(
                isinstance(self.myClass, NewClass)
            ).to(
                equal(True)
            )