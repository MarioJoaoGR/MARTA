require "formatador"

RSpec.describe Formatador do

  it "handles nil argument gracefully" do
    formatador = Formatador.new
    expect { formatador.redisplay_line(nil) }.not_to raise_error
  end

end
