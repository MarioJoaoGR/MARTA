require "formatador/progressbar"
RSpec.describe Formatador::ProgressBar do
  describe "#initialize" do
    it "initializes with default start value of 0" do
      progress_bar = Formatador::ProgressBar.new(10)
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(10)
    end

    it "initializes with the specified start value" do
      progress_bar = Formatador::ProgressBar.new(10, start: 5)
      expect(progress_bar.current).to eq(5)
      expect(progress_bar.total).to eq(10)
    end

  end
end
