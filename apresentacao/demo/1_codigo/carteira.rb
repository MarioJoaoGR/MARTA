require_relative "movimento"

class Carteira
  def initialize
    @mov = Movimento.new
  end

  def saldo
    @mov.total
  end

  def resumo
    "Saldo actual: #{saldo}"
  end
end
