require "formatador"

RSpec.describe Formatador do
  describe "#display_line" do
    it "handles valid input for display_line method" do
      expect(Formatador.display_line("Hello [bold]World[reset]")).to eq nil
    end


  end
end
