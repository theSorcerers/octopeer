class Repository < ApplicationRecord
  validates :owner, uniqueness: {scope: [:name, :platform]}
end
