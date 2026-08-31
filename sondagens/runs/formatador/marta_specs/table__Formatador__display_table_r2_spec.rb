require "formatador"

RSpec.describe Formatador do
  describe "#display_table" do
    it "handles valid inputs (Happy Path)" do
      hashes = [{name: "Alice", age: 30}, {name: "Bob", age: 25}]
      expect { Formatador.display_table(hashes) }.not_to raise_error
    end


  end
end
