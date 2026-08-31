require "formatador"

RSpec.describe Formatador do
  describe "#length" do
    it "calculates length correctly for single-byte characters" do
      expect(Formatador.new.send(:length, "hello")).to eq("hello".length)
    end

    it "handles nil argument by calculating byte length" do
      expect { Formatador.new.send(:length, nil) }.not_to raise_error
      expect(Formatador.new.send(:length, nil)).to eq(0)
    end

    it "handles non-string type argument by calculating byte length" do
      expect { Formatador.new.send(:length, 123) }.not_to raise_error
      expect(Formatador.new.send(:length, 123)).to eq(3)
    end
  end
end
