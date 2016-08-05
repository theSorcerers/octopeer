class PullRequest < ApplicationRecord
  belongs_to :repository
  validates :repository, uniqueness: { scope: :pull_request_number }
end
