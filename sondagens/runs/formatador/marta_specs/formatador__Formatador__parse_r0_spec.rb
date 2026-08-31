require "formatador"

RSpec.describe Formatador do
  describe "#parse" do


    it "handles empty string input gracefully" do
      expect(Formatador.parse("")).to eq("")
    end
  end
end
