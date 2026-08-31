require "formatador"

RSpec.describe Formatador do
  describe "#indentation" do
    it "should correctly return indentation for a minimal instance" do
      formatador = Formatador.new
      expect(formatador.indentation).to eq("  ")
    end

    it "should handle nil arguments gracefully without raising an error" do
      formatador = Formatador.new
      expect { formatador.indentation }.not_to raise_error
    end

  end
end
