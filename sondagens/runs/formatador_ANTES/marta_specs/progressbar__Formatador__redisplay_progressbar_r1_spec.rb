require "formatador/progressbar"
RSpec.describe Formatador do
  describe "#redisplay_progressbar" do
    it "handles valid inputs correctly" do
      formatador = Formatador.new
      allow(formatador).to receive(:redisplay)
      allow(formatador).to receive(:new_line)
      
      expect { formatador.redisplay_progressbar(10, 100) }.not_to raise_error
    end


  end
end
