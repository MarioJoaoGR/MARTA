class Movimento
  def initialize(valores = [])
    @valores = valores
  end

  def total
    @valores.sum
  end

  def juntar(outro)
    Movimento.new(@valores + outro.total)
  end
end
