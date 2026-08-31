require "formatador"

RSpec.describe Formatador do
  describe "#display" do
    it "handles valid inputs correctly" do
      formatador = Formatador.new
      expect(formatador.display("Hello, World!")).to eq nil
    end

  end

end
