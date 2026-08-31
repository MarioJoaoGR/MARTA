require "formatador"

RSpec.describe Formatador do
  describe "#set_title" do
    it "sets a valid title and returns nil" do
      # Setup
      instance = Formatador.new
      
      # Exercise
      result = instance.set_title("New Title")
      
      # Verify
      expect(result).to be_nil
    end

  end
end
