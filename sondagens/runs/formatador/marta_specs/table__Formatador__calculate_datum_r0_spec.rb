require "formatador/table"
RSpec.describe Formatador do
  describe "#calculate_datum" do
    let(:hash) { { header1: "value1", nested: { key2: "value2" } } }
    
    it "retrieves a value directly from the hash using a valid header" do
      expect(subject.send(:calculate_datum, :header1, hash)).to eq("value1")
    end


    it "returns an empty string when the provided header does not match any key in the hash" do
      expect(subject.send(:calculate_datum, :non_existent_header, hash)).to eq("")
    end
  end
end
