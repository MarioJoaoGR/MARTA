require "formatador"

RSpec.describe Formatador do
  describe "#display" do
    it "handles valid input correctly" do
      formatador = Formatador.new
      expect { formatador.display("Hello, World!") }.not_to raise_error
    end


  end
end
