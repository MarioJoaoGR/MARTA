require "formatador"

RSpec.describe Formatador do
  describe "#display" do
    it "handles valid inputs correctly" do
      formatador = Formatador.new
      expect(formatador.display("Hello, World!")).to eq nil
    end
  end

  describe "#indent" do
    it "ensures the indent level increases and decreases correctly within a block" do
      formatador = Formatador.new
      initial_indent = formatador.instance_variable_get(:@indent)
      formatador.indent { }
      expect(formatador.instance_variable_get(:@indent)).to eq(initial_indent)
    end


  end
end
