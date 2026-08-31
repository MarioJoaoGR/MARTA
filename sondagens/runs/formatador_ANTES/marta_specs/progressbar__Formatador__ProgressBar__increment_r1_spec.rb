require "formatador/progressbar"
RSpec.describe Formatador::ProgressBar do
  describe "#initialize" do
    it "initializes with default start value when only total is provided" do
      progress_bar = Formatador::ProgressBar.new(10)
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(10)
    end

    it "initializes with specified start value when total and opts are provided" do
      progress_bar = Formatador::ProgressBar.new(10, {start: 5})
      expect(progress_bar.current).to eq(5)
      expect(progress_bar.total).to eq(10)
    end


    it "converts non-integer total to integer and initializes" do
      progress_bar = Formatador::ProgressBar.new("10")
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(10)
    end
  end

  describe "#increment" do

    it "does not increment when complete" do
      progress_bar = Formatador::ProgressBar.new(5, {start: 5})
      progress_bar.increment
      expect(progress_bar.current).to eq(5)
    end

  end
end
