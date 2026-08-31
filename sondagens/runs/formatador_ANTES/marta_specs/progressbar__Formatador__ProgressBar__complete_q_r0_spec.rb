require "formatador/progressbar"
RSpec.describe Formatador::ProgressBar do
  describe "#initialize" do
    it "initializes with standard setup" do
      progress_bar = Formatador::ProgressBar.new(10)
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(10)
    end

    it "initializes with total set to zero" do
      progress_bar = Formatador::ProgressBar.new(0)
      expect(progress_bar.current).to eq(0)
      expect(progress_bar.total).to eq(0)
    end

  end
end
