require "formatador/progressbar"
RSpec.describe Formatador::ProgressBar do
  describe "#initialize" do
    it "initializes with valid total and optional start value" do
      progress_bar = Formatador::ProgressBar.new(100)
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(100)
      expect(progress_bar.opts).to be_empty
    end

    it "initializes with zero as total" do
      progress_bar = Formatador::ProgressBar.new(0)
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(0)
      expect(progress_bar.opts).to be_empty
    end

  end
end
