require "formatador"

RSpec.describe Formatador do
  describe "#display_lines" do
    it "handles valid input and displays lines correctly" do
      formatador = Formatador.new
      expect(formatador.display_lines(["Hello, World!", "This is a test."])).to eq nil
    end

    it "handles edge cases such as nil and empty arrays gracefully" do
      formatador = Formatador.new
      expect { formatador.display_lines(nil) }.not_to raise_error
      expect { formatador.display_lines([]) }.not_to raise_error
    end

  end
end
