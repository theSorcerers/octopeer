class Repository < ApplicationRecord
  has_many :pull_requests
  validates :owner, uniqueness: { scope: [:name, :platform] }
end
