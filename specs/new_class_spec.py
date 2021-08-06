from mamba import description, context, it, before
from expects import expect, equal
from package import new_class

with description("Given a NewClass") as self:
    with context("When nothing else happens"):
        with it("Should be an instance of NewClass"):
            myClass = new_class.NewClass()
            expect(
                isinstance(myClass, new_class.NewClass)
            ).to(
                equal(True)
            )