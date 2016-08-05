class PullRequestSerializer < ActiveModel::Serializer
  attributes :id, :pull_request_number
  belongs_to :repository
end
