require "formatador"

RSpec.describe Formatador do
  describe "#display_lines" do
    it "handles an empty array gracefully" do
      # Setup
      instance = Formatador.new
      allow(instance).to receive(:display_line)
      
      # Exercise
      result = instance.display_lines([])
      
      # Verify
      expect([*result]).to eq([])
    end
  end
end
