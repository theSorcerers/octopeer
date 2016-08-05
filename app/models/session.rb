class Session < ApplicationRecord
  belongs_to :pull_request
  belongs_to :user
end
